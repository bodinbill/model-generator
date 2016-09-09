GET_METHOD_TEMPLATE = """	/**
	 * Gets %s.
	 *
	 * @return %s
	 */
	%s get%s();"""

SET_METHOD_TEMPLATE = """	/**
	 * Sets %s.
	 *
	 * @param %s
	 *            %s
	 */
	void set%s(%s %s);"""

IS_METHOD_TEMPLATE = """	/**
	 * Checks if this is %s or not.
	 *
	 * @return {@code true} if this is %s
	 */
	%s is%s();"""

INTERFACE_TEMPLATE = """package com.wongnai.domain.model.%s;

/**
 * %s.
 *
 * @author %s
 */
public interface %s extends %s<%s> {
%s
}
"""

IMPLEMENT_TEMPLATE = """package com.wongnai.domain.model.%s.internal;

/**
 * Default implementation of {@link %s}.
 *
 * @author %s
 */
public class %sImpl extends %s<%s> implements %s {
	private static final long serialVersionUID = 1L;
%s
%s
}
"""

GET_METHOD_IMPL_TEMPLATE = """
	@Override
	public %s get%s() {
		return %s;
	}"""

SET_METHOD_IMPL_TEMPLATE = """
	@Override
	public void set%s(%s %s) {
		this.%s = %s;
	}"""

IS_METHOD_IMPL_TEMPLATE = """
	@Override
	public %s is%s() {
		return %s;
	}"""

TEST_TEMPLATE = """package com.wongnai.domain.model.%s.internal;

public class %sImplTest {
	@Before
	public void setUp() {
            underTest = new %sImpl();
	}

%s
}
"""

TEST_METHOD_TEMPLATE = """	@Test
	public void test%s() {
		Assert.assertThat(underTest.get%s(),CoreMatchers.nullValue());
		underTest.set%s(%s);
		Assert.assertThat(underTest.get%s(),CoreMatchers.equalTo(%s));
	}"""

TEST_IS_METHOD_TEMPLATE = """	@Test
	public void test%s() {
		Assert.assertThat(underTest.is%s(),CoreMatchers.equalTo(false));
		underTest.set%s(true);
		Assert.assertThat(underTest.is%s(),CoreMatchers.equalTo(true));
	}"""

TEST_REPOSITORY_HIBERNATE_TEMPLATE = """package com.wongnai.infrastructure.hibernate;

public class {0}RepositoryHibernateTest
		extends AbstractHibernateRepositoryTestCase<{0}RepositoryHibernate, {0}, Long> {{

	@Override
	protected {0} createTestEntity(Long key) {{
		{0}Impl testEntity = {0}Impl.create();

		AbstractEntity.setId(testEntity, key);

		return testEntity;
	}}

	@Override
	protected Long createTestKey() {{
		return 5L;
	}}

	@Override
	protected {0}RepositoryHibernate createUnderTest() {{
		return new {0}RepositoryHibernate();
	}}

	@Override
	protected Set<String> getExpectedAssociations() {{
		return null;
	}}
}}
"""

FORM_TEMPLATE = """package com.wongnai.web.admin.{packet};
/**
 * The base form of {{@link {interface}}}.
 *
 * @author {auther}
 */
public class CreateOrUpdate{interface}Form extends AbstractCreateOrUpdateForm<{interface}, {entitykey}> {{
{variable}

	/**
	 * Fills inputs to the given {name}.
	 *
	 * @param {camel}
	 *            {name}
	 */
	protected void fill({interface} {camel}) {{
		{fill}
	}}
}}
"""

FORM_GET_METHOD_IMPL_TEMPLATE = """	/**
	 * Gets {callname}.
	 *
	 * @return {callname}
	 */
	public {ftype} get{upper}() {{
		return {name};
	}}"""

FORM_SET_METHOD_IMPL_TEMPLATE = """	/**
	 * Sets {callname}.
	 *
	 * @param {name}
	 *            {callname}
	 */
	public void set{upper}({ftype} {name}) {{
		this.{name} = {name};
	}}"""

FORM_IS_METHOD_IMPL_TEMPLATE = """	/**
	 * Checks if this is {callname} or not.
	 *
	 * @return {{@code true}} if this is %s
	 */
	public {ftype} is{upper}() {{
		return {name};
	}}"""

FILTER_TEMPLATE = """package com.wongnai.domain.model.{packet};

/**
 * {interface} filter.
 *
 * @author {auther}
 */
public class {interface}Filter implements ValueObject<String> {{
        private static final long serialVersionUID = 1L;
{variable}

	/**
	 * Checks if this filter is required or not. A filter is required only if at
	 * least one property is set.
	 *
	 * @return {{@code true}} if this filter is required
	 */
	public boolean isRequired() {{
		return {required};
	}}

	@Override
	public int hashCode() {{
		HashCodeBuilder b = new HashCodeBuilder();

		b{hashAppends};

		return b.toHashCode();
	}}

	@Override
	public boolean equals(Object obj) {{
		if (obj == null) {{
			return false;
		}} else if (obj == this) {{
			return true;
		}} else if (!(obj instanceof {interface}Filter)) {{
			return false;
		}} else {{
			{interface}Filter rhs = (({interface}Filter) obj);
			EqualsBuilder b = new EqualsBuilder();

{equalsAppends}

			return b.isEquals();
		}}
	}}
	
	@Override
	public String toString() {{
		return ReflectionToStringBuilder.toString(this);
	}}
	
	@Override
	public String getValue() {{
		return toString();
	}}
}}
"""

FIlTER_HAS_METHOD_TEMPLATE = """	/**
	 * Checks if {callname} is set or not.
	 *
	 * @return {{@code true}} if {callname} is set.
	 */
	public boolean has{upper}() {{
		return {name} != null;
	}}"""

FILTER_TEST_TEMPLATE = """package com.wongnai.domain.model.{packet};

public class {interface}FilterTest {{
	private {interface}Filter underTest;
	private {interface}Filter underTest2;

	@Before
	public void setUp() {{
		underTest = new {interface}Filter();
	}}
	
{testunit}
	
	@Test
	public void testToString() throws Exception {{
		fillProperties(underTest);

		Assert.assertThat(underTest.toString(), CoreMatchers.equalTo(ReflectionToStringBuilder.toString(underTest)));
		Assert.assertThat(underTest.getValue(), CoreMatchers.equalTo(underTest.toString()));
	}}

	@Test
	public void testEqualsAll() {{
		setUpUnderTestsForEquals();

		Assert.assertThat(underTest.equals(underTest2), CoreMatchers.equalTo(true));
		Assert.assertThat(underTest2.equals(underTest), CoreMatchers.equalTo(true));
	}}

	private void setUpUnderTestsForEquals() {{
		underTest2 = new {interface}Filter();

		fillProperties(underTest);
		fillProperties(underTest2);
	}}

	private void fillProperties({interface}Filter filter) {{
{properties}
	}}

	@Test
	public void testEqualsSome() {{
		underTest2 = new {interface}Filter();

		underTest.setRegionId(TestCase.ANY_LONG);
		underTest2.setRegionId(TestCase.ANY_LONG);

		Assert.assertThat(underTest.equals(underTest2), CoreMatchers.equalTo(true));
		Assert.assertThat(underTest2.equals(underTest), CoreMatchers.equalTo(true));
	}}

	@Test
	public void testEqualsSame() {{
		Assert.assertThat(underTest.equals(underTest), CoreMatchers.equalTo(true));
	}}
 
	private void assertNotEquals() {{
		Assert.assertThat(underTest.equals(underTest2), CoreMatchers.equalTo(false));
		Assert.assertThat(underTest2.equals(underTest), CoreMatchers.equalTo(false));
	}}

	@Test
	public void testNotEqualsNull() {{
		Assert.assertThat(underTest.equals(null), CoreMatchers.equalTo(false));
	}}

	@Test
	public void testNotEqualsOther() {{
		Assert.assertThat(underTest.equals(new Object()), CoreMatchers.equalTo(false));
	}}

	@Test
	public void testHash() {{
		underTest2 = new {interface}Filter();

		underTest.setRegionId(TestCase.ANY_LONG);
		underTest2.setRegionId(TestCase.ANY_LONG);

		Assert.assertThat(underTest2.hashCode(), CoreMatchers.equalTo(underTest.hashCode()));
	}}

	@Test
	public void testRequire() {{
		fillProperties(underTest);
		Assert.assertThat(underTest.isRequired(), CoreMatchers.equalTo(true));
{requires}
	}}
}}
"""

FILTER_METHOD_TEST = """	@Test
	public void test{upper}() {{
		Assert.assertThat(underTest.get{upper}(), CoreMatchers.nullValue());

		underTest.set{upper}(TestCase.ANY_{uppertype});

		Assert.assertThat(underTest.get{upper}(), CoreMatchers.equalTo(TestCase.ANY_{uppertype}));
	}}
 
	@Test
	public void testHas{upper}() {{
		Assert.assertThat(underTest.has{upper}(), CoreMatchers.equalTo(false));
		underTest.set{upper}(null);
		Assert.assertThat(underTest.has{upper}(), CoreMatchers.equalTo(false));

		underTest.set{upper}(TestCase.ANY_{uppertype});
		Assert.assertThat(underTest.has{upper}(), CoreMatchers.equalTo(true));
	}}
	
	@Test
	public void test{upper}NotEquals() {{
		setUpUnderTestsForEquals();

		underTest2.set{upper}(null);

		assertNotEquals();
	}}"""
